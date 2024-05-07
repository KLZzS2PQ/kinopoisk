function getCookie(name) {
    if (!document.cookie) {
        return null;
    }

    const xsrfCookies = document.cookie.split(';')
        .map(c => c.trim())
        .filter(c => c.startsWith(name + '='));

    if (xsrfCookies.length === 0) {
        return null;
    }
    return decodeURIComponent(xsrfCookies[0].split('=')[1]);
}


async function sendPost(url, data) {
    const csrfToken = getCookie('csrftoken');
    console.log(csrfToken)
    return fetch(url, {
        method: "POST", body: JSON.stringify(data), headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        }
    }).then(response => {
        return response.json()
    })
}

// async function sendPost(url, data) {
//     const request = new XMLHttpRequest();
//     request.open('POST', url);
//     const header = "X-CSRFToken";
//     const token = getCookie('csrftoken');
//     request.setRequestHeader(header, token);
//     const dataInf = new FormData();
//     for (const key in data) {
//         dataInf.append(key, data[key]);
//     }
//     request.send(dataInf);
//     console.log("Request sent");
//     request.onload = () => {
//         const received = request.responseText;
//         console.log(JSON.parse(received))
//         return JSON.parse(received);
//     };
//     return null
// };














