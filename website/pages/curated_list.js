let gridApiCL;
const gridOptionsCL = {
  rowData: [],
  autoSizeStrategy: {
    type: "fitCellContents"
  },
  tooltipShowMode: "whenTruncated",
  tooltipShowDelay: 1000,
  columnDefs: [
    {
      headerName: "To Pocket",
      field: "url",
      cellRenderer: PocketCellLinkRendererCL,
      cellStyle: {textAlign: "center"},
      maxWidth: 120,
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
  pagination: true,
  defaultColDef: {
    filter: true
  }
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


function PocketCellLinkRendererCL(params) {
  let url = params.value;
  let link = `
    <a
      href="https://getpocket.com/edit?url=${url}"
    >
    <img src="common/pocket.png" alt="save to pocket" class="pocket-img">
  </a>`;
  return link;
}


gridApiCL = agGrid.createGrid(document.querySelector("#CuratedListGrid"), gridOptionsCL);
fetch("data/curated_list.json")
  .then((response) => response.json())
  .then((data) => gridApiCL.setGridOption("rowData", data));
