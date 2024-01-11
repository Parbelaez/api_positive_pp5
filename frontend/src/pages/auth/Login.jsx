import { useState } from "react";
import axios from "axios";
// useHistory has been replaced by useNavigate in react-router-dom v6
import { Link, useNavigate } from "react-router-dom";

import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import { Alert } from "react-bootstrap";

import { useSetCurrentUser } from "../../contexts/CurrentUserContext";
import { setTokenTimestamp } from "../../utils/utils";

function Login() {
    const setCurrentUser = useSetCurrentUser();

    const [loginData, setLoginData] = useState({
        username: "",
        password: "",
    });
    // To avoid using dot notation to access the properties of the loginData object
    const { username, password } = loginData;

    const [errors, setErrors] = useState({});

    let navigate = useNavigate();

    const handleSubmit = async (event) => {
        event.preventDefault();

        try {
            const { data } = await axios.post(
                "/dj-rest-auth/login/",
                loginData
            );
            setCurrentUser(data.user);
            // setAccessToken(data);
            setTokenTimestamp(data);
            localStorage.setItem("access_token", data?.access_token)
            navigate("/");
        } catch (error) {
            // The question mark will check if there is a response object in the error object
            // If there is a response object, then the data property will be accessed
            // If there is no response object, then the error object will be logged to the console
            console.log("error.response?.data", error.response?.data, error);
            setErrors(error.response?.data);
        }
    };

    const handleChange = (event) => {
        // handleChange for all fields
        setLoginData({
            ...loginData,
            [event.target.name]: event.target.value,
        });
    };

    return (
        <div>
            <h1>Log In</h1>
            <Form onSubmit={handleSubmit}>
                <Form.Group className="mb-3" controlId="username">
                    <Form.Label className="d-none">username</Form.Label>
                    <Form.Control
                        type="text"
                        placeholder="username"
                        name="username"
                        value={username}
                        onChange={handleChange}
                    />
                </Form.Group>
                {errors.username?.map((message, idx) => (
                    <Alert key={idx} variant="warning">
                        {message}
                    </Alert>
                ))}

                <Form.Group className="mb-3" controlId="password">
                    <Form.Label className="d-none">Password</Form.Label>
                    <Form.Control
                        type="password"
                        placeholder="Password"
                        name="password"
                        value={password}
                        onChange={handleChange}
                    />
                </Form.Group>
                {errors.password1?.map((message, idx) => (
                    <Alert key={idx} variant="warning">
                        {message}
                    </Alert>
                ))}
                <Button variant="primary" type="submit">
                    Log In
                </Button>
                {/* Used when the passwords don't match */}
                {errors.non_field_errors?.map((message, idx) => (
                    <Alert key={idx} variant="warning">
                        {message}
                    </Alert>
                ))}
            </Form>
            <Link to="/signup">
                Don't have an account? <span>Sign up now!</span>
            </Link>
        </div>
    );
}

export default Login;
