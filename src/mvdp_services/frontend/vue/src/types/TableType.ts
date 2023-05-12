export default interface HeaderType {
    text: string
    value: string
}

type Item = string | number

export default interface TableType {
    headers: HeaderType[],
    items: Item[]   
}

