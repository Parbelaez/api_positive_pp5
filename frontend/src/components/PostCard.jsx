import OverlayTrigger from "react-bootstrap/OverlayTrigger";
import Tooltip from "react-bootstrap/Tooltip";
import { Link } from "react-router-dom";
import Card from "react-bootstrap/Card";
import { useCurrentUser } from "../contexts/CurrentUserContext";
import { axiosRes } from "../api/axiosDefaults";

const PostCard = (props) => {
    const {
        // The fields of the serializer, not the model
        id,
        owner,
        title,
        content,
        image,
        like_id,
        num_tops,
        num_likes,
        num_dislikes,
        postPage,
        setPosts,
    } = props;

    const currentUser = useCurrentUser();
    const is_owner = currentUser?.username === owner;

    const handleLike = async () => {
        try {
            const { data } = await axiosRes.post('/likes/', { post: id });
            setPosts((prevPosts) => ({
                ...prevPosts,
                results: prevPosts.results.map((post) => {
                    return post.id === id
                        ? {
                            ...post,
                            likes_count: post.likes_count + 1,
                            like_id: data.id
                        }
                        : post;
                }),
            }));
        } catch (error) {
                console.log(error)
        }
    }

    const handleUnlike = async () => {
        try {
            await axiosRes.delete(`/likes/${ like_id }`);
            setPosts((prevPosts) => ({
                ...prevPosts,
                results: prevPosts.results.map((post) => {
                    return post.id === id
                        ? {
                            ...post,
                            likes_count: post.likes_count - 1,
                            like_id: null,
                        }
                        : post;
                }),
            }));
        } catch (error) {
            console.log(error);
        }
    };

    return (
        <Card style={{ width: "18rem" }}>
            <Card.Img variant="top" src={image} />
            <Card.Body>
                <Card.Title>{title}</Card.Title>
                <Card.Text>{content}</Card.Text>
                {/* is the logged in user the owner and the post page exists? */}
                <p>{is_owner && postPage && "..."}</p>
                <div>
                    {is_owner ? (
                        <OverlayTrigger
                            placement="top"
                            overlay={
                                <Tooltip>You can't like your own post!</Tooltip>
                            }
                        >
                            <i className="far fa-heart" />
                        </OverlayTrigger>
                    ) : like_id ? (
                        <span onClick={handleUnlike}>
                            <i className={`fas fa-heart`} />
                        </span>
                    ) : currentUser ? (
                        <span onClick={handleLike}>
                            <i className={`far fa-heart`} />
                        </span>
                    ) : (
                        <OverlayTrigger
                            placement="top"
                            overlay={<Tooltip>Log in to like posts!</Tooltip>}
                        >
                            <i className="far fa-heart" />
                        </OverlayTrigger>
                    )}
                    {num_tops}
                    <Link to={`/posts/${id}`}>
                        <i className="fa-regular fa-thumbs-up" />
                    </Link>
                    {num_likes}
                    {num_dislikes}
                </div>
            </Card.Body>
        </Card>
    );
};

export default PostCard;
