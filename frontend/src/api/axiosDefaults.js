import axios from "axios";

    // New api
axios.defaults.baseURL = "https://api-positive-a53d71b6a573.herokuapp.com";
    // API Localhost
// axios.defaults.baseURL = "http://localhost:8000";
    // GitPod
// axios.defaults.baseURL = "https://8000-parbelaez-apipositivepp-5xtfwrcwnaj.ws-eu107.gitpod.io/"
// CI Deployment
// axios.defaults.baseURL = "https://drf-api-cnc7.onrender.com/";
//PauloMoments
// axios.defaults.baseURL = "https://drf-api-fork-ci-2734278030fe.herokuapp.com/";

axios.defaults.headers.post["Content-Type"] = "multipart/form-data";
axios.defaults.withCredentials = true;

export const axiosReq = axios.create();
export const axiosRes = axios.create();