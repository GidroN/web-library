function handleForm(event) {
    if (event.submitter.name === "action" && event.submitter.value === "register") {
        event.target.action = "/register";
    } else if (event.submitter.name === "action" && event.submitter.value === "login") {
        event.target.action = "/login";
    }
}