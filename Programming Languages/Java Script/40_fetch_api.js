let api = fetch("api/url");

api.then((response) => {
    console.log(response.status);
    console.log(response.ok);

    return response.json();
}).then((value) => {
    console.log(value);
})