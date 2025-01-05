function loadDoc() {
    const a = new XMLHttpRequest();
    a.onload = function(){
        document.getElementById("trail").innerHTML = this.responseText;
    }
    a.open("GET", "/static/profile/testfile.txt");
    a.send();
}

document.addEventListener('DOMContentLoaded',() => {
    const table = document.getElementById("profile-table");
    let = currentlyEditingRow = null;

    table.addEventListener('click', (event) =>{
        const target = event.target;
        const row = target.closest('tr');
        if (!row) return;

        if (target.classList.contains('edit-btn')) {
            if (currentlyEditingRow && currentlyEditingRow !== row){
                resetRow(currentlyEditingRow);
            }
            currentlyEditingRow = row;

            row.querySelectorAll('.editable').forEach(cell => {
                const value = cell.innerText;
                cell.innerHTML = `<input type='text' value='${value}' />`
            });
            
            target.style.display = "none";
            row.querySelector(".delete-btn").style.display = "none"
            row.querySelector(".add-btn").style.display = "none"
            row.querySelector(".save-btn").style.display = "inline-block"
            row.querySelector(".cancel-btn").style.display = "inline-block"             
        }
        if (target.classList.contains('save-btn')) {
            const id = row.getAttribute("data-id");
            const updateData = {};
            row.querySelectorAll(".editable").forEach((cell, index) => {
                const input = cell.querySelector("input");
                if (input) {
                    updateData[`field_${index + 1}`] = input.value;// console.log(`updated _${index + 1}`, input.value);
                    cell.innerHTML = input.value;
                }
            });
            console.log('updated Ajax;', updateData );
            target.style.display = "none";
            row.querySelector(".delete-btn").style.display = "inline-block"
            row.querySelector(".add-btn").style.display = "inline-block"
            row.querySelector(".save-btn").style.display = "none"
            row.querySelector(".cancel-btn").style.display = "none" 

            fetch(`/edit/${id}/`, {
                method : "POST",
                headers : {
                    "content-Type" : "application/json",
                    "X-CSRFToken": getCookie("csrftoken"),
                },
                body : JSON.stringify(updateData),
            })
                .then(response => response.json())
                .then(data => {
                    console.log("Server Response:", data);
                    if (data.success) {
                        alert("Changes saved successfully!");
                    } 
                    else {
                        alert("Failed to save changes.");
                    }
                });
            currentlyEditingRow = null;
            target.style.display = "none";
            row.querySelector(".edit-btn").style.display = "inline-block";
            row.querySelector(".delete-btn").style.display = "inline-block";
            row.querySelector(".add-btn").style.display = "inline-block";
            row.querySelector(".cancel-btn").style.display = "none";
        }

        if (target.classList.contains("cancel-btn")) {
            resetRow(row);
            currentlyEditingRow = null;
        }

    });

    function resetRow(row) {
        row.querySelectorAll(".editable").forEach(cell => {
            const input = cell.querySelector("input");
            if (input) {
                cell.innerHTML = input.value; // Reset to input's value
            }
        });
        row.querySelector(".edit-btn").style.display = "inline-block";
        row.querySelector(".delete-btn").style.display = "inline-block";
        row.querySelector(".add-btn").style.display = "inline-block";
        row.querySelector(".save-btn").style.display = "none";
        row.querySelector(".cancel-btn").style.display = "none";
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === name + "=") {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        // console.log("CSRF token retrieved:", cookieValue);
        return cookieValue;
    }
    
});

function showMore(profileId) {
    const moreDiv = document.getElementById(`more-${profileId}`);
    if (moreDiv.style.display === "none") {
        moreDiv.style.display = "block";
    } else {
        moreDiv.style.display = "none";
    }
}