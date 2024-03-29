class WebServices {
    constructor() {}

    /**
     * This method wraps Fetch API for simplifying it
     * @param url: string - Requested resource URL
     * @param method: string - Method name, default value js GET
     * @returns {Promise<{success: boolean, response: any, error: string} | {success: boolean, response: [], error: *}>}
     */
    fetchResource(url, method = 'GET') {
        return fetch(url, { method: method })
            .then(response => response.json())
            .then(jsonResponse => ( this.defaultResponse(jsonResponse) ))
            .catch(error => ( this.defaultResponse(undefined, error.message) ));
    }

    /**
     * Fetch multiple resources at once, response structure may vary base on the resources response
     * @param urls
     * @returns {Promise<({success: boolean, response: *, error: string}|{success: boolean, response: *[], error: *})[]>|Promise<unknown>}
     */
    fetchResources(urls = []) {
        if (Array.isArray(urls)) {
            urls = Array.from(urls, url => url.toString());
            return Promise.all(urls.map(url => this.fetchResource(url)));
        }
        return new Promise((resolve, reject) => reject( this.defaultResponse() ));
    }

   /** defaultResponse( response = { success: false, data: [] }, errorMessage = '') {
        return { ...response, error: errorMessage };
    }*/
}

const ws = new WebServices();