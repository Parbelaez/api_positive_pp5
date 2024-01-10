import { useEffect, useState } from "react";
import PostCard from "../components/PostCard";
import { useParams } from "react-router";
import { axiosReq } from "../api/axiosDefaults";
import { Container } from "react-bootstrap";


function PostPage() {
    const { id } = useParams();
    const [post, setPost] = useState({ results: [] });

    useEffect(() => {
        const handleMount = async () => {
            try {
                const [{ data: post }] = await Promise.all([
                    axiosReq.get(`/posts/${id}`),
                ]);
                setPost({ results: [post] });
                console.log(post);
            } catch (error) {
                console.log(error);
            }
        }
        handleMount();
    }, [id]);

    return (
        <Container>
            <PostCard {...post.results[0]} setPosts={setPost} postPage/>
        </Container>
    );
}

export default PostPage