let gridApiCL;
const gridOptionsCL = {
  rowData: [],
  getRowId: params => params.data.title,
  autoSizeStrategy: {type: "fitCellContents"},
  tooltipShowMode: "whenTruncated",
  tooltipShowDelay: 1000,
  pagination: true,
  enableCellTextSelection: true,
  defaultColDef: {filter: true},
  rowClassRules: {
    "row-background-grey": "data.background_color == 'GREY'",
    "row-background-pink": "data.background_color == 'PINK'",
    "row-background-red": "data.background_color == 'RED'",
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
      cellRenderer: TitleCellLinkRendererCL,
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


function onFilterTextBoxChangedCL() {
  gridApiCL.setGridOption(
    "quickFilterText",
    document.getElementById("curated-list-filter").value,
  );
}


function TitleCellLinkRendererCL(params) {
  const a = document.createElement("a");
  a.textContent = params.value;
  a.target = "_blank";
  a.rel = "noopener noreferrer";
  a.href = `${params.data.url}`;
  return a;
}


document.addEventListener('keydown', function(event) {
  if (event.key === '/') {
    var filter = document.getElementById('curated-list-filter');
    filter.setSelectionRange(0, filter.value.length);
    filter.focus();
    event.preventDefault();
  }
});


gridApiCL = agGrid.createGrid(document.querySelector("#CuratedListGrid"), gridOptionsCL);
fetch("data/curated_list.json")
  .then((response) => response.json())
  .then((data) => gridApiCL.setGridOption("rowData", data));
