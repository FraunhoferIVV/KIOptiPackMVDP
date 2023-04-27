#!/bin/bash

# stop on error
set -euo pipefail

function registerParticipant() {
  local participantName="$1"
  local participantDid="$2"
  local address="$3"

  echo "Registering $participantName at $address with $participantDid"
  java -jar registration-service-cli.jar \
              -d="did:web:10.62.13.225%3A7070:registration-service" \
              --http-scheme \
              -k="/resources/vault/$participantName/private-key.pem" \
              -c="$participantDid" \
               participants add
}

function seedVerifiedCredentials() {
  local participantName="$1"
  local participantDid="$2"
  local region="$3"
  local address="$4"

   for subject in '"region": "'$region'"'
   do
     echo "Seeding VC for $participantName: $subject at $address with $participantDid"
     java -jar identity-hub-cli.jar \
                 -s="http://$address:7171/api/v1/identity/identity-hub" \
                 vc add \
                 -c="{ $subject }" \
                 -b="$participantDid" \
                 -i="did:web:10.62.13.225%3A7070:gaia-x" \
                 -k="/resources/vault/gaia-x/private-key.pem"
   done
}

function seedAndRegisterParticipant() {
  local participantName="$1"
  local region="$2"
  local address="$3"
  local participantDid="did:web:10.62.13.225%3A7070:$participantName"

  # seed vc for participant
  seedVerifiedCredentials "$participantName" "$participantDid" "$region" "$address"

  # Register dataspace participants
  registerParticipant "$participantName" "$participantDid" "$address"
}

function awaitParticipantRegistration() {
  local participantName="$1"
  local region="$2"
  local address="$3"
  local participantDid="did:web:10.62.13.225%3A7070:$participantName"

  cmd="java -jar registration-service-cli.jar \
                  -d=did:web:10.62.13.225%3A7070:registration-service \
                  --http-scheme \
                  -k=/resources/vault/$participantName/private-key.pem \
                  -c=$participantDid \
                  participants get"

  # Wait for participant registration.
  ./validate_onboarding.sh "$participantDid" "$cmd"
}

# Read participants from participants.json file.
# $participants will contain participants and regions in a shell readable format e.g.:
# 'company1' 'eu' \n 'company2' 'eu' \n 'company3' 'us'
participants=$(jq -r '.include | map([.participant, .region, .address])[] | @sh' /common-resources/participants-VM.json)

# Seed VCs and register participants.
while read -r i; do
  # shellcheck disable=SC2086 # disable IDE warning: allow word splitting on jq @sh output
  eval seedAndRegisterParticipant $i
done <<< "$participants"

# Await registrations of participants.
while read -r i; do
  # shellcheck disable=SC2086 # disable IDE warning: allow word splitting on jq @sh output
  eval awaitParticipantRegistration $i
done <<< "$participants"

# flag for healthcheck by Docker
echo "finished" > finished.flag
echo "Finished successfully! Keep the container running."

# keep the container running
sleep infinity
