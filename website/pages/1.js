let gridApi__1;
const gridOptions__1 = {
  rowData: [],
  getRowId: params => params.data.title,
  autoSizeStrategy: {type: "fitCellContents"},
  tooltipShowMode: "whenTruncated",
  tooltipShowDelay: 1000,
  pagination: true,
  paginationPageSize: 1000,
  paginationPageSizeSelector: false,
  enableCellTextSelection: true,
  defaultColDef: {filter: true},
  rowClassRules: {
    "row-background-grey": "data.comment == 'FRIN'",
  },

  columnDefs: [
    {
      headerName: "#",
      valueGetter: params => params.node.rowIndex + 1,
      maxWidth: 75,
      sortable: false,
      filter: false,
    },
    {
      field: "title",
      cellRenderer: TitleCellLinkRenderer__1,
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
  ],
};


function onFilterTextBoxChanged__1() {
  gridApi__1.setGridOption(
    "quickFilterText",
    document.getElementById("filter__1").value,
  );
}


function TitleCellLinkRenderer__1(params) {
  const a = document.createElement("a");
  a.textContent = params.value;
  a.target = "_blank";
  a.rel = "noopener noreferrer";
  a.href = params.data.url;
  return a;
}


document.addEventListener('keydown', function(event) {
  if (event.key === '/') {
    var filter = document.getElementById('filter__1');
    filter.setSelectionRange(0, filter.value.length);
    filter.focus();
    event.preventDefault();
  }
});


gridApi__1 = agGrid.createGrid(document.querySelector("#Grid__1"), gridOptions__1);
fetch("data/curated_list.json")
  .then((response) => response.json())
  .then((data) => gridApi__1.setGridOption("rowData", data));
