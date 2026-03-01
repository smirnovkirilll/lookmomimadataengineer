import {
    applyQuickFilter,
    createBaseGridOptions,
} from "../common/utils.js";
import {
    columns__1,
    c_rules__1,
} from "./columns__curated_list.js";


let gridApi__1;
const gridOptions__1 = {
    ...createBaseGridOptions(),
    columnDefs: columns__1,
    rowClassRules: c_rules__1,
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
