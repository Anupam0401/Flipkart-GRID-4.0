//Data fetch from API
function fetching() {
    let url = "https://fakestoreapi.com/products";
    fetch(url)
        .then(res => res.json()).then(data => {
            addData(data);
        });
}
fetching();
//Add Chart and cards in html
function addData(data) {

    if (data.length > 0) {
        renderData(data)
    }
    else {
        showPopUp();
    }
}
//show pop up if API is empty
function showPopUp() {
    swal({
        title: "OOPS",
        text: "No trends are there right now ",
        icon: "warning",
        dangerMode: true,
    })
        .then((willDelete) => {
            if (willDelete) {
                window.location = "../index.html";
            }
        });
}
//render data array
function renderData(data) {
    let completeData = "";
    let count = 1;
    let xlabelsArray = [];
    let ylabelsArray = [];
    data.map(val => {
        let subCategory = ((val.sub_category == null) || (val.sub_category == undefined)) ? "" : val.sub_category;
        let trendingScore = ((val.trend_score == null) || (val.trend_score == undefined)) ? "" : val.trend_score;
        let vertical = ((val.vertical == null) || (val.vertical == undefined)) ? "" : `<button type="button" class="btn btn-secondary badge" 
        data-toggle="tooltip" data-placement="right">
        ${val.vertical}
        </button>`;
        let type = ((val.trending_attribute_type == null) || (val.trending_attribute_type == undefined)) ? "" : `<button type="button" class="btn btn-secondary badge" 
        data-toggle="tooltip" data-placement="right">
        ${val.trending_attribute_type}
        </button>`;
        let value = ((val.trending_attribute_value == null) || (val.trending_attribute_value == undefined)) ? "" : `<button type="button" class="btn btn-secondary badge" data-toggle="tooltip" data-placement="right">
        ${val.trending_attribute_type}
        </button>`;
        let postImg = ((val.Post_Image == null) || (val.Post_Image == undefined)) ? `${val.Post_url}` : val.Post_Image;


        ylabelsArray.push(val.title);
        xlabelsArray.push(val.id);

        
        completeData +=
            `<div class="card mb-3 m-3 card-deck" style="max-width: 500px; box-shadow: 10px 10px 5px 0px rgb(71, 68, 68); " id="category_card">
            <div class="row no-gutters"  >
                <div class="col-md-6 d-flex align-items-center justify-content-center" >
                    <div class="img-area">
                    <a href=${val.Post_url}>
                        <img  src=${postImg} class="card-img py-2 image" alt="..." height="300px">
                    </a>
                        <div class="overlay">
                            <div class="image-text"> 
                                <div class="text-center" >
                                    <p style="color:#282c34;font-weight:bolder;font-size:small;" aria-hidden="true">
                                    <a href="${val.Post_url}">
                                        <i class="fa fa-external-link p-3"  style="font-size:large;background-color:white;color:#282c34;border-radius:4px; 
                                        box-shadow: 10px 10px 5px 0px rgb(71, 68, 68);">
                                        </i>
                                    </a>
                                    </p>
                                    <p class="text-center p-1" style="color:white;font-weight:bolder;font-size:15px;line-height: initial;">See the post</p>
                                </div>
                            </div>
                        </div>
                </div>
            </div>
            <div class="col-md-6 d-flex align-items-center justify-content-center">
                <div class="card-body">
                    <h5 class="card-title text-center"><span style="color:#898989;font-weight: bold;font-size:xx-large;">#</span><b  style="color:#282c34">${count++}</b></h5>
                    <h4 class="card-title  text-center" style="color:#282c34;font-weight: bold; ">${subCategory}</h4>
                    <p class="card-title  text-center" style="color:#282c34;font-weight: bold; ">Trending Score:${trendingScore}</p>
                    <p class="card-text text-center d-flex flex-wrap justify-content-center">
                    ${vertical}
                    ${type}
                    ${value}
                    </p>
                    <p class="text-center p-1" style="color:#282c34;font-weight:bolder;font-size:15px;line-height: initial;">See the matched product</p>
                    <div class="text-center" >
                    <p style="color:#282c34;font-weight:bolder;font-size:x-large;" aria-hidden="true">
                    <a href="${val.Flipkart_url}">
                        <i class="fa fa-external-link p-3"  style="background-color:#61dafb;color:#282c34;border-radius:4px; 
                        box-shadow: 10px 10px 5px 0px rgb(71, 68, 68);">
                        </i>
                    </a>
                    </p>
                    </div>
                    </div>
                </div>
            </div>
            </div>`
    });
    addChart(xlabelsArray, ylabelsArray);
    document.getElementById("cards").innerHTML = completeData;
}
//add chart
function addChart(xlabelsArray, ylabelsArray) {
    document.getElementById("chart-section").innerHTML = `
    <div class="row p-4  d-flex justify-content-center" id="chart-bg">
      <div id="chart-heading" class="pb-3">Trends Analysis</div>
      <div class="col-md-6"  id="Chart" max-height="400">
        <canvas id="myChart"class="p-3"></canvas>
      </div>
  </div>
    `;
    chartMake(xlabelsArray, ylabelsArray);
}
//make chart code from chart.js
function chartMake(xlabelsArray, ylabelsArray) {
    let ctx = document.getElementById('myChart').getContext('2d');
    let myChart = new Chart(ctx, {
        type: 'line',

        data: {
            labels: ylabelsArray,
            datasets: [{
                label: 'Trend score Vs Subcategory',
                data: xlabelsArray,
                backgroundColor: "white",
                borderColor:
                    'rgba(255, 99, 132, 1)',
                borderWidth: 3
            }]
        },
        options: {
            scales: {
                x: {
                    ticks: {
                        color: "black"
                    },

                },
                y: {
                    ticks: {
                        color: "black"
                    },
                    font: {
                        weight: "bolder"
                    },
                    beginAtZero: true,
                }
            }
        }
    });

}
//fetch data after given interval
setInterval(fetching, 2700000);