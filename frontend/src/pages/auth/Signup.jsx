import { useState } from "react";
// useHistory has been replaced by useNavigate in react-router-dom v6
import { Link, useNavigate } from "react-router-dom";

import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import axios from "axios";
import { Alert } from "react-bootstrap";

function Signup() {
    const [signUpData, setSignUpData] = useState({
        email: "",
        username: "",
        password1: "",
        password2: "",
    });
    // To avoid using dot notation to access the properties of the signUpData object
    const { email, username, password1, password2 } = signUpData;

    const [errors, setErrors] = useState({});

    let navigate = useNavigate();

    const handleChange = (event) => {
        // handleChange for all fields
        setSignUpData({
            ...signUpData,
            [event.target.name]: event.target.value,
        });
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            console.log("try submit signUpData");
            await axios.post("/dj-rest-auth/registration/", signUpData);
            navigate("/login");
            console.log("finished submit signUpData");
        } catch (error) {
            // The question mark will check if there is a response object in the error object
            // If there is a response object, then the data property will be accessed
            // If there is no response object, then the error object will be logged to the console
            console.log("error.response?.data", error.response?.data, error);
            setErrors(error.response?.data);
        }
    };

    return (
        <div>
            <h1>Sign Up</h1>
            <Form onSubmit={handleSubmit}>
                <Form.Group className="mb-3" controlId="email">
                    <Form.Label className="d-none">Email</Form.Label>
                    <Form.Control
                        type="email"
                        placeholder="Enter email"
                        name="email"
                        value={email}
                        onChange={handleChange}
                    />
                    <Form.Text className="text-muted">
                        We'll never share your email with anyone else.
                    </Form.Text>
                </Form.Group>
                {errors.email?.map((message, idx) => (
                    <Alert key={idx} variant="warning">
                        {message}
                    </Alert>
                ))}
                <Form.Group className="mb-3" controlId="username">
                    <Form.Label className="d-none">username</Form.Label>
                    <Form.Control
                        type="text"
                        placeholder="username"
                        name="username"
                        value={username}
                        onChange={handleChange}
                    />
                    <Form.Text className="text-muted">
                        How would you like other users to see you.
                    </Form.Text>
                </Form.Group>
                {errors.username?.map((message, idx) => (
                    <Alert key={idx} variant="warning">
                        {message}
                    </Alert>
                ))}

                <Form.Group className="mb-3" controlId="password1">
                    <Form.Label className="d-none">Password</Form.Label>
                    <Form.Control
                        type="password"
                        placeholder="Password"
                        name="password1"
                        value={password1}
                        onChange={handleChange}
                    />
                </Form.Group>
                {errors.password1?.map((message, idx) => (
                    <Alert key={idx} variant="warning">
                        {message}
                    </Alert>
                ))}
                <Form.Group className="mb-3" controlId="password2">
                    <Form.Label className="d-none">Confirm Password</Form.Label>
                    <Form.Control
                        type="password"
                        placeholder="Confirm Password"
                        name="password2"
                        value={password2}
                        onChange={handleChange}
                    />
                </Form.Group>
                {errors.password2?.map((message, idx) => (
                    <Alert key={idx} variant="warning">
                        {message}
                    </Alert>
                ))}
                <Button variant="primary" type="submit">
                    Sign Up
                </Button>
                {/* Used when the passwords don't match */}
                {errors.non_field_errors?.map((message, idx) => (
                    <Alert key={idx} variant="warning">
                        {message}
                    </Alert>
                ))}
            </Form>
            <Link to="/login">
                Already have an account? <span>Login</span>
            </Link>
        </div>
    );
}

export default Signup;
