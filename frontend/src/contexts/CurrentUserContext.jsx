import { createContext, useContext, useEffect, useMemo, useState } from "react";
import axios from "axios";
import { axiosReq, axiosRes } from "../api/axiosDefaults";
import { useNavigate } from "react-router-dom";
import { removeTokenTimestamp, shouldRefreshToken } from "../utils/utils";

export const CurrentUserContext = createContext();
export const SetCurrentUserContext = createContext();

export const useCurrentUser = () => useContext(CurrentUserContext);
export const useSetCurrentUser = () => useContext(SetCurrentUserContext);

export const CurrentUserProvider = ({ children }) => {
    console.log("Current user provider 1");
    const [currentUser, setCurrentUser] = useState(null);
    const navigate = useNavigate();

    //!console log the current user provider - is it changing?
    console.log("Current user provider 2");

    const handleMount = async () => {
        console.log("handle mount");
        try {
            const { data } = await axiosRes.get("dj-rest-auth/user/");
            console.log("Context data", data);
            setCurrentUser(data);
        } catch (error) {
            console.log(error);
        }
    };

    useEffect(() => {
        handleMount();
    }, []);

    // It needs to be placed here, because we need it to run before
    // the children are rendered
    useMemo(() => {
        axiosReq.interceptors.request.use(
            async (config) => {
                if (shouldRefreshToken()) {
                    console.log("should refresh token")
                    try {
                        await axios.post("/dj-rest-auth/token/refresh/");
                    } catch (error) {
                        console.log("ISSUE IS HERE")
                        setCurrentUser((prevCurrentUser) => {
                            if (prevCurrentUser) {
                                navigate("/login");
                            }
                            return null;
                        });
                        console.log("Remove token timestamp by request interceptor");
                        removeTokenTimestamp();
                        return config;
                    }
                }
                return config;
            },
            (error) => {
                return Promise.reject(error);
            }
        );

        axiosRes.interceptors.response.use(
            (response) => response,
            async (error) => {
                if (error.response?.status === 401) {
                    try {
                        await axios.post("/dj-rest-auth/token/refresh/");
                    } catch (error) {
                        setCurrentUser((prevCurrentUser) => {
                            if (prevCurrentUser) {
                                navigate("/login");
                            }
                            return null;
                        });
                        console.log(
                            "Remove token timestamp by response interceptor"
                        );
                        removeTokenTimestamp();
                    }
                    return axios(error.config);
                }
                return Promise.reject(error);
            }
        );
    }, [navigate]);

    return (
        <CurrentUserContext.Provider value={currentUser}>
            <SetCurrentUserContext.Provider value={setCurrentUser}>
                {children}
            </SetCurrentUserContext.Provider>
        </CurrentUserContext.Provider>
    );
};
