class WebServices {
    constructor() {}

    /**
     * This method wraps Fetch API for simplifying it
     * @param url [string] - Requested resource URL
     * @param method [string] - Method name, default value is GET
     * @returns {Promise<{success: boolean, response: any, error: string} | {success: boolean, response: [], error: *}>}
     */
    fetchResource(url, method = 'GET') {
        return fetch(url, { method: method })
            .then(response => response.json())
            .then(jsonResponse => ( { success: true, response: jsonResponse, error: '' } ))
            .catch(error => ( { success: false, response: [], error: error.message } ));
    }
}

const ws = new WebServices();