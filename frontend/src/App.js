import styles from './App.module.css';
import NavBar from './components/NavBar';
import Container from 'react-bootstrap/Container';
import { Routes, Route } from 'react-router-dom';
// pages
import Dashboard from './pages/Dashboard';
import Login from './pages/auth/Login';
import Signup from './pages/auth/Signup';
import PostPage from './pages/PostPage';
import CreatePlace from './pages/CreatePlace';
import About from './pages/About';
import NotFound from './pages/NotFound';
// axios
import './api/axiosDefaults'
// import { useCurrentUser } from './contexts/CurrentUserContext';

function App() {
  // const currentUser = useCurrentUser();
  // const profile_id = currentUser?.profile_id || "";
  return (
    <div className={styles.App}>
      <NavBar />
      <Container className={styles.Main}>
        <Routes>
          <Route path="/" element={<Dashboard message="No results found. Please, adjust the search keyword."/>} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/posts/:id" element={<PostPage />} />
          <Route path="/create-place" element={<CreatePlace />} />
          <Route path="/about" element={<About />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </Container>
    </div>
  );
}

export default App;
