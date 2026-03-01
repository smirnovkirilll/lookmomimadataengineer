import {
  titleLinkRenderer,
  applyQuickFilter,
  createBaseGridOptions,
} from "../common/utils.js";


let gridApi__1;
const gridOptions__1 = {
  ...createBaseGridOptions(),
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
  ],
};


document.addEventListener('keydown', function(event) {
  if (event.key === '/') {
    var filter = document.getElementById('filter__1');
    filter.setSelectionRange(0, filter.value.length);
    filter.focus();
    event.preventDefault();
  }
});


document.getElementById("filter__1").addEventListener("input", () =>
    applyQuickFilter(gridApi__1, "filter__1")
  );


gridApi__1 = agGrid.createGrid(document.querySelector("#Grid__1"), gridOptions__1);
fetch("data/curated_list.json")
  .then((response) => response.json())
  .then((data) => gridApi__1.setGridOption("rowData", data));
