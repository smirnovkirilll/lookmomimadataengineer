let gridApiCL;
const gridOptionsCL = {
  rowData: [],
  autoSizeStrategy: {
    type: "fitCellContents"
  },
  columnDefs: [
    { field: "topic" },
    { field: "type of content" },
    { field: "language" },
    {
      field: "title",
      cellRenderer: TitleCellLinkRendererCL,
      maxWidth: 700,
    },
    {
      headerName: "To Pocket",
      field: "url",
      cellRenderer: PocketCellLinkRendererCL,
      cellStyle: {textAlign: "center"}
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
