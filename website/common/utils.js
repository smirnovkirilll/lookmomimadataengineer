export function titleLinkRenderer(params) {
    const anchor = document.createElement("a");
    anchor.textContent = params.value;
    anchor.target = "_blank";
    anchor.rel = "noopener noreferrer";
    anchor.href = params.data.url;

    return anchor;
}


export function applyQuickFilter(api, inputId) {
    const input = document.getElementById(inputId);
    api.setGridOption("quickFilterText", input.value);
}


export function createBaseGridOptions() {
    return {
        rowData: [],
        getRowId: params => params.data.title,
        autoSizeStrategy: {type: "fitCellContents"},
        tooltipShowMode: "whenTruncated",
        tooltipShowDelay: 1000,
        pagination: true,
        paginationPageSize: 1000,
        paginationPageSizeSelector: false,
        enableCellTextSelection: true,
        defaultColDef: {
            filter: true,
            resizable: true,
            sortable: true,
        },
    };
}
