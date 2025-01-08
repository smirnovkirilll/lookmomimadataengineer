let gridApiRD;
const gridOptionsRD = {
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
  ],
  pagination: true,
  defaultColDef: {
    filter: true
  }
};


function onFilterTextBoxChangedRD() {
  gridApiRD.setGridOption(
    "quickFilterText",
    document.getElementById("reddit-digest-filter").value,
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


gridApiRD = agGrid.createGrid(document.querySelector("#RedditDigestGrid"), gridOptionsRD);
fetch("data/reddit-digest.json")
  .then((response) => response.json())
  .then((data) => gridApiRD.setGridOption("rowData", data));
