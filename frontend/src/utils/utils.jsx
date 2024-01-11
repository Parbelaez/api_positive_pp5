import { jwtDecode } from "jwt-decode"

export const setAccessToken = (data) => {
    localStorage.setItem("accessToken", data?.access);
};

export const setTokenTimestamp = (data) => {
    const refreshTokenTimestamp = jwtDecode(data?.refresh).exp;
    localStorage.setItem("refreshTokenTimestamp", refreshTokenTimestamp);
};

export const shouldRefreshToken = () => {
    const refreshtokenexists = !!localStorage.getItem("refreshTokenTimestamp");
    return !!localStorage.getItem("refreshTokenTimestamp");
};

export const removeTokenTimestamp = () => {
    localStorage.removeItem("refreshTokenTimestamp");
};