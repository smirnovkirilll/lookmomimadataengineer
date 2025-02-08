let gridApiRD;
const gridOptionsRD = {
  rowData: [],
  columnDefs: [
    {
      field: "subreddit",
      maxWidth: 150,
    },
    {
      field: "tag",
      maxWidth: 100,
    },
    {
      field: "author",
      maxWidth: 150,
      },
    {
      field: "title",
      cellRenderer: TitleCellLinkRendererRD,
      minWidth: 500,
      maxWidth: 700,
    },
    {
      headerName: "To pocket",
      field: "external_url",
      cellRenderer: PocketCellLinkRendererRD,
      cellStyle: {textAlign: "center"},
      maxWidth: 120,
    },
    {
      field: "comments",
      cellStyle: {textAlign: "center"},
      maxWidth: 120,
    },
    {
      field: "up_votes",
      cellStyle: {textAlign: "center"},
      maxWidth: 120,
    },
    {
      field: "down_votes",
      cellStyle: {textAlign: "center"},
      maxWidth: 120,
    },
    {
      field: "created_utc_dttm",
      cellStyle: {textAlign: "center"},
      maxWidth: 170,
    }
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


function TitleCellLinkRendererRD(params) {
  let title = params.value;
  let url = params.data.reddit_url;
  let link = `
    <a
      href="${url}"
    >
    ${title}
  </a>`;
  return link;
}


function PocketCellLinkRendererRD(params) {
  let url = params.value;
  let link = `
    <a
      href="https://getpocket.com/edit?url=${url}"
    >
    <img src="common/pocket.png" alt="save to pocket" class="pocket-img">
  </a>`;
  return link;
}


gridApiRD = agGrid.createGrid(document.querySelector("#RedditDigestGrid"), gridOptionsRD);
fetch("data/reddit_digest.json")
  .then((response) => response.json())
  .then((data) => gridApiRD.setGridOption("rowData", data));
