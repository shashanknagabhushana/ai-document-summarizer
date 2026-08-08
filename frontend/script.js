const fileInput =
    document.getElementById("fileInput");

const fileName =
    document.getElementById("fileName");

const summarizeButton =
    document.getElementById("summarizeButton");

const loading =
    document.getElementById("loading");

const result =
    document.getElementById("result");

const error =
    document.getElementById("error");

const summaryText =
    document.getElementById("summaryText");

const documentName =
    document.getElementById("documentName");

const characterCount =
    document.getElementById("characterCount");


let selectedFile = null;


// --------------------------------------------------
// File selection
// --------------------------------------------------

fileInput.addEventListener(
    "change",
    function () {

        selectedFile = fileInput.files[0];

        if (!selectedFile) {

            fileName.textContent = "";

            summarizeButton.disabled = true;

            return;
        }


        fileName.textContent =
            `Selected: ${selectedFile.name}`;


        summarizeButton.disabled = false;


        result.classList.add("hidden");

        error.classList.add("hidden");
    }
);


// --------------------------------------------------
// Summarize document
// --------------------------------------------------

summarizeButton.addEventListener(
    "click",
    async function () {

        if (!selectedFile) {
            return;
        }


        const formData =
            new FormData();


        formData.append(
            "file",
            selectedFile
        );


        // Show loading
        loading.classList.remove(
            "hidden"
        );


        result.classList.add(
            "hidden"
        );


        error.classList.add(
            "hidden"
        );


        summarizeButton.disabled = true;


        try {

            const response =
                await fetch(
                    "/upload",
                    {
                        method: "POST",
                        body: formData
                    }
                );


            const data =
                await response.json();


            // Check API response
            if (!response.ok) {

                throw new Error(
                    data.detail ||
                    "Something went wrong."
                );
            }


            // Display summary
            summaryText.textContent =
                data.summary;


            // Display filename
            documentName.textContent =
                `File: ${data.filename}`;


            // Display character count
            characterCount.textContent =
                `${data.characters} characters`;


            // Show result
            result.classList.remove(
                "hidden"
            );

        }


        catch (err) {

            error.textContent =
                err.message;


            error.classList.remove(
                "hidden"
            );

        }


        finally {

            loading.classList.add(
                "hidden"
            );


            summarizeButton.disabled =
                false;
        }
    }
);
