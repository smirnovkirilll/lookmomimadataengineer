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
      tooltipField: "title",
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
  let title = params.value;
  let url = params.data.url;
  let link = `
    <a
      href="${url}"
    >
    ${title}
  </a>`;
  return link;
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
