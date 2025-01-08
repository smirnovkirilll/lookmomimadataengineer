let gridApiCL;
const gridOptionsCL = {
  rowData: [],
  columnDefs: [
    { field: "mission" },
    {
        headerName: "save to pocket",
        field: "mission",
        cellRenderer: CellLinkRenderer,
        cellStyle: {textAlign: 'center'}
    },
    { field: "company" },
    { field: "location" },
    { field: "date" },
    { field: "price" },
    { field: "successful" },
    { field: "rocket" },
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


function CellLinkRenderer(params) {
    let keyData = params.value;
    let newLink = `
        <a
            href="https://getpocket.com/edit?url=https://habr.com/ru/articles/871582/"
//            href="https://getpocket.com/edit?url=${keyData}" TODO
        >
        <img src="common/pocket.png" alt="save to pocket" class="pocket-img">
    </a>`;
     return newLink;
}


gridApiCL = agGrid.createGrid(document.querySelector("#CuratedListGrid"), gridOptionsCL);
fetch("data/curated-list.json")
  .then((response) => response.json())
  .then((data) => gridApiCL.setGridOption("rowData", data));
