const createTodo = async () => {
    let options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title: "title",
            body: "body-message",
            userId: 1,
        })
    }
    let p = await fetch("api/url", options);
    let response = await p.json();
    return response;
}

const mainFunc = async () => {
    let todo = await createTodo();
    console.log(todo);
}

mainFunc();
