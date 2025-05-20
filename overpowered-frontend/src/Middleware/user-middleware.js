async function getUserById(userId) {
    const user = await fetch(`http://localhost:3001/users/${userId}/`,
        {
            method : "GET",
            headers : {"Content-Type" : "application/json"},
            credentials : true
        }
    );

    if (user.ok) {
        return user;
    }

    return null;
}

async function getUserByName(name) {
    const user = await fetch(`http://localhost:3001/users/${name}/`,
        {
            method : "GET",
            headers : {"Content-Type" : "application/json"},
            credentials : true
        }
    );

    if (user.ok) {
        return user;
    }

    return null;
}

async function createUser(protoUser) {
    const user = await fetch(`http://localhost:3001/users/`,
        {
            method : "POST",
            body : JSON.stringify(protoUser),
            headers : {"Content-Type" : "application/json"},
            credentials : true
        }
    );

    if (user.ok) {
        return user;
    }

    return null;
}