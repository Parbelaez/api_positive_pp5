import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import NavDropdown from "react-bootstrap/NavDropdown";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import logo_color_trimmed from "../assets/logo_color_trimmed.png";
import { NavLink, Link } from "react-router-dom";
import styles from "../styles/NavBar.module.css";
import {
    useCurrentUser,
    useSetCurrentUser,
} from "../contexts/CurrentUserContext";
import Avatar from "./Avatar";
import axios from "axios";
import { useClickOutsideToggle } from "../hooks/useClickOutsideToggle";
import { removeTokenTimestamp } from "../utils/utils";

const NavBar = () => {
    const currentUser = useCurrentUser();
    const setCurrentUser = useSetCurrentUser();

    console.log(currentUser)

    const { expanded, setExpanded, ref } = useClickOutsideToggle();

    const handleSignOut = async () => {
        try {
            await axios.post("dj-rest-auth/logout/");
            setCurrentUser(null);
            removeTokenTimestamp();
        } catch (err) {
            console.log(err);
        }
    };

    const addAvatar = (
        <>
            <NavLink
                className={styles.NavLink}
                // Back ticks are used to interpolate the profile id
                to={`/profiles/${currentUser?.profile_id}`}
            >
                <Avatar src={currentUser?.profile_image} height={40} />
            </NavLink>
        </>
    );

    const loggedInIcons = (
        <>
            <NavDropdown title="Places" id="basic-nav-dropdown">
                <NavDropdown.Item>
                    <Link to="/places">All Places</Link>
                </NavDropdown.Item>
                <NavDropdown.Item>
                    <Link to="/create-place">Create New Place</Link>
                </NavDropdown.Item>
            </NavDropdown>
            <NavDropdown title="Posts" id="basic-nav-dropdown">
                <NavDropdown.Item>
                    <Link to="/posts">All Posts</Link>
                </NavDropdown.Item>
                <NavDropdown.Item>
                    <Link to="/new_post">Create New Post</Link>
                </NavDropdown.Item>
            </NavDropdown>
            <NavLink
                // activeClassName has been deprecated in react router 6
                className={
                    ({ isActive }) =>
                        "{styles.NavLink}" + (isActive ? "{styles.Active}" : "")
                }
                to="/login"
                onClick={handleSignOut}
            >
                Logout
            </NavLink>
        </>
    );

    const loggedOutIcons = <></>;

    return (
        <Navbar
            className={styles.NavBar}
            expanded={expanded}
            expand="md"
            fixed="top"
        >
            <Container>
                <NavLink to="/">
                    <Navbar.Brand>
                        <img
                            src={logo_color_trimmed}
                            alt="logo"
                            height="45"
                        ></img>
                    </Navbar.Brand>
                </NavLink>
                <Navbar.Toggle
                    ref={ref}
                    onClick={() => setExpanded(!expanded)}
                    aria-controls="navbarScroll"
                />
                <Navbar.Collapse id="navbarScroll">
                    <Nav
                        className="me-auto my-2 my-lg-0"
                        style={{ maxHeight: "100px" }}
                        navbarScroll
                    >
                        {currentUser ? loggedInIcons : loggedOutIcons}
                        <NavLink
                            className={({ isActive }) =>
                                "{styles.NavLink}" +
                                (isActive ? "{styles.Active}" : "")
                            }
                            to="/about"
                        >
                            About
                        </NavLink>
                        {currentUser && addAvatar}
                    </Nav>
                    <Form className="d-flex">
                        <Form.Control
                            type="search"
                            placeholder="Search"
                            className="me-2"
                            aria-label="Search"
                        />
                        <Button variant="outline-success">Search</Button>
                    </Form>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
};

export default NavBar;
