import { titleLinkRenderer } from "../common/utils.js";


export const columns__1 = [
    {
        headerName: "#",
        valueGetter: params => params.node.rowIndex + 1,
        maxWidth: 75,
        sortable: false,
        filter: false,
    },
    {
        field: "title",
        cellRenderer: titleLinkRenderer,
        minWidth: 500,
        maxWidth: 600,
        tooltipValueGetter: params => params.value,
    },
    { field: "topic" },
    { field: "type of content" },
    { field: "language" },
    {
        field: "author",
        minWidth: 200,
        maxWidth: 600,
    },
    {
        field: "comment",
        minWidth: 300,
        maxWidth: 600,
        tooltipField: "comment",
    },
];


export const c_rules__1 = {
    "row-background-grey": "data.comment == 'FRIN'",
};
