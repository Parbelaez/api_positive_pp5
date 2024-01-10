import axios from "axios";


// axios.defaults.baseURL = "https://api-positive-a53d71b6a573.herokuapp.com";

axios.defaults.baseURL = "/api";
axios.defaults.headers.post["Content-Type"] = "multipart/form-data";
axios.defaults.withCredentials = true;

export const axiosReq = axios.create();
export const axiosRes = axios.create();