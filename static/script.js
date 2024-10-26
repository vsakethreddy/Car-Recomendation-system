const body = document.querySelector("body"),
      modeToggle = body.querySelector(".mode-toggle");
      sidebar = body.querySelector("nav");
      sidebarToggle = body.querySelector(".sidebar-toggle");

let getMode = localStorage.getItem("mode");
if(getMode && getMode ==="dark"){
    body.classList.toggle("dark");
}

let getStatus = localStorage.getItem("status");
if(getStatus && getStatus ==="close"){
    sidebar.classList.toggle("close");
}

modeToggle.addEventListener("click", () =>{
    body.classList.toggle("dark");
    if(body.classList.contains("dark")){
        localStorage.setItem("mode", "dark");
    }else{
        localStorage.setItem("mode", "light");
    }
});

sidebarToggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    if(sidebar.classList.contains("close")){
        localStorage.setItem("status", "close");
    }else{
        localStorage.setItem("status", "open");
    }
})


// JS for ANALYTICS PAGE

// document.addEventListener("DOMContentLoaded", function() {
//     // Sample data (replace it with your startup's real data)
//     const ordersData = [10, 15, 8, 20, 12];
//     const revenueData = [100, 150, 80, 200, 120];

//     // Get the canvas element
//     const ordersChartCanvas = document.getElementById("ordersChart").getContext("2d");

//     // Create a bar chart
//     const ordersChart = new Chart(ordersChartCanvas, {
//         type: "bar",
//         data: {
//             labels: ["Month 1", "Month 2", "Month 3", "Month 4", "Month 5"],
//             datasets: [{
//                 label: "Orders",
//                 data: ordersData,
//                 backgroundColor: "#3498db",
//                 borderWidth: 1
//             }]
//         },
//         options: {
//             scales: {
//                 y: {
//                     beginAtZero: true
//                 }
//             }
//         }
//     });

//     // Display summary data
//     document.getElementById("totalOrders").innerText = ordersData.reduce((a, b) => a + b, 0);
//     document.getElementById("totalRevenue").innerText = revenueData.reduce((a, b) => a + b, 0);
// });


// JS for SALES 

// document.addEventListener("DOMContentLoaded", function() {
//     // Sample sales data (replace it with your startup's real data)
//     const salesData = [
//         { date: "2024-01-01", product: "Cleaning Service", quantity: 5, pricePerUnit: 30 },
//         { date: "2024-01-05", product: "Cooking Service", quantity: 3, pricePerUnit: 40 },
//         // Add more sales data as needed
//     ];

//     // Get the table body element
//     const salesTableBody = document.querySelector("#salesTable tbody");

//     // Populate the sales table with data
//     salesData.forEach(sale => {
//         const row = document.createElement("tr");
//         row.innerHTML = `
//             <td>${sale.date}</td>
//             <td>${sale.product}</td>
//             <td>${sale.quantity}</td>
//             <td>$${sale.pricePerUnit}</td>
//             <td>$${sale.quantity * sale.pricePerUnit}</td>
//         `;
//         salesTableBody.appendChild(row);
//     });

//     // Calculate and display total sales
//     const totalSales = salesData.reduce((total, sale) => total + sale.quantity * sale.pricePerUnit, 0);
//     document.getElementById("totalSales").innerText = `$${totalSales.toFixed(2)}`;
// });
