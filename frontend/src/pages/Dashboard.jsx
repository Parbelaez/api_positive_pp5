import PostCard from "../components/PostCard";
import { useState, useEffect } from "react";
import { axiosReq } from "../api/axiosDefaults";
import { useLocation } from "react-router";


function Dashboard({ message, filter = "" }) {
    const [posts, setPosts] = useState({ results: [] });
    const [hasLoaded, setHasLoaded] = useState(false);
    const { pathname } = useLocation();

    useEffect(() => {
        const dashboard = async () => {
            try {
                const { data } = await axiosReq.get(`/posts/?${ filter }`);
                console.log(data);
                setPosts(data);
                setHasLoaded(true);
            } catch (error) {
                console.log(error);
            }
        }
        setHasLoaded(false);
        dashboard();
    }, [filter, pathname]);
    return (
        <div>
            <h1>Positive Posts</h1>
                <div className="row">
                {hasLoaded ? (
                    <>
                        {posts.results.length ? (
                            posts.results.map((post) => (
                                <div className="col-md-4" key={post.id}>
                                    <PostCard
                                        key={post.id}
                                        {...post}
                                        setPosts={setPosts}
                                    />
                                </div>
                            ))
                        ) : (
                            <div className="col-md-12">
                                <h3>No posts found</h3>
                            </div>
                        )}
                    </>
                    ) : (
                        <div className="col-md-12">
                            <h3>Loading...</h3>
                        </div>
                )}
            </div>
        </div>
    )
}

export default Dashboard;
