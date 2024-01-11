import { useState, useEffect, useRef } from "react";
import { axiosReq } from "../api/axiosDefaults";
import { useNavigate } from "react-router-dom";
import Alert from "react-bootstrap/Alert";

// For this form, we used a different approach to the one taught in the course.
// There is no destructuring of the postData object, and the handleChange function
// is used for all fields.
// Even though, the approach is not as efficient and it is more repetitive, it
// is easier to understand and to debug. And it serves as a good example of how
// the many ways to do things in React and coding overall (logic practice).

function CreatePlace() {
    const [errors, setErrors] = useState({});
    const [countries, setCountry] = useState([]);
    const [cities, setCity] = useState([]);
    var cityCountries = {};
    const [countryAndCity, setCountryAndCity] = useState({});
    const imageInput = useRef(null);
    let navigate = useNavigate();

    const [postData, setPostData] = useState({
        place_name: "",
        place_type: "",
        address: "",
        country: "",
        city: "",
        website: "",
        phone_number: "",
        description: "",
        image: "",
    });

    // Fetches all countries and their cities from a third party API
    // More on this in the README.md file
    useEffect(
        () => {
            fetch("https://countriesnow.space/api/v0.1/countries")
                .then((res) => res.json())
                .then((data) => {
                    setCountry(data.data);
                    data.data.forEach((country) => {
                        cityCountries[country.country] = country.cities;
                    });
                })
                // Used to avoid the error of the city field being empty when the country is selected
                .then(() => {
                    setCountryAndCity(cityCountries);
                });
        },
        // eslint-disable-next-line react-hooks/exhaustive-deps
        []
    );

    const handleChange = (event) => {
        // handleChange for all fields
        setPostData({
            ...postData,
            [event.target.name]: event.target.value,
        });
        // handleChange for country field... city field is updated based on country
        if (event.target.name === "country") {
            setCity(countryAndCity[event.target.value]);
        }
    };

    const handleChangeImage = (event) => {
        // handleChange for image field
        if (event.target.files.length) {
            setPostData({
                ...postData,
                image: URL.createObjectURL(event.target.files[0]),
            });
        }
    };

    const handleSelect = (event) => {
        setPostData({
            ...postData,
            [event.target.name]: event.target.value,
        });
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData();

        formData.append("place_name", postData.place_name);
        formData.append("place_type", postData.place_type);
        formData.append("address", postData.address);
        formData.append("country", postData.country);
        formData.append("city", postData.city);
        formData.append("website", postData.website);
        formData.append("phone_number", postData.phone_number);
        formData.append("description", postData.description);
        formData.append("image", imageInput.current.files[0]);

        try {
            const { data } = await axiosReq.post("/places/", formData);
            navigate(`/places/${data.id}`);
        } catch (err) {
            console.log(err);
            if (err.response?.status !== 401) {
                setErrors(err.response?.data);
            }
        }
    };

    return (
        <div>
            <h1>Create Place Page</h1>
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="place_name">Place Name</label>
                    <input
                        type="text"
                        className="form-control"
                        id="place_name"
                        name="place_name"
                        value={postData.place_name}
                        onChange={handleChange}
                    />
                </div>
                {errors?.title?.map((message, idx) => (
                    <Alert variant="warning" key={idx}>
                        {message}
                    </Alert>
                ))}
                <div className="form-group">
                    <label htmlFor="place_type">Place Type</label>
                    <select
                        name="place_type"
                        className="form-control"
                        id="place_type"
                        onChange={handleSelect}
                    >
                        <option value="" selected disable hidden>
                            Choose the type of place
                        </option>
                        <option value="restaurant">Restaurant</option>
                        <option value="bar">Bar</option>
                        <option value="hotel">Hotel</option>
                        <option value="museum">Museum</option>
                        <option value="park">Park</option>
                        <option value="beach">Beach</option>
                        <option value="other">Other</option>
                    </select>
                </div>
                {errors?.title?.map((message, idx) => (
                    <Alert variant="warning" key={idx}>
                        {message}
                    </Alert>
                ))}
                <div className="form-group">
                    <label htmlFor="address">Address</label>
                    <input
                        type="text"
                        className="form-control"
                        id="address"
                        name="address"
                        value={postData.address}
                        onChange={handleChange}
                    />
                </div>
                {errors?.title?.map((message, idx) => (
                    <Alert variant="warning" key={idx}>
                        {message}
                    </Alert>
                ))}
                <div className="form-group">
                    <label htmlFor="country">Country</label>
                    <select
                        className="form-control"
                        id="country"
                        name="country"
                        value={postData.country}
                        onChange={handleChange}
                    >
                        <option value="">Select a country</option>
                        {countries.map((country) => (
                            <option value={country.country}>
                                {country.country}
                            </option>
                        ))}
                    </select>
                </div>
                {errors?.title?.map((message, idx) => (
                    <Alert variant="warning" key={idx}>
                        {message}
                    </Alert>
                ))}
                <div className="form-group">
                    <label htmlFor="city">City</label>
                    <select
                        className="form-control"
                        id="city"
                        name="city"
                        value={postData.city}
                        onChange={handleChange}
                    >
                        <option value="">Select a city</option>
                        {cities.map((city) => (
                            <option value={city}>{city}</option>
                        ))}
                    </select>
                </div>
                {errors?.title?.map((message, idx) => (
                    <Alert variant="warning" key={idx}>
                        {message}
                    </Alert>
                ))}
                <div className="form-group">
                    <label htmlFor="website">Website</label>
                    <input
                        type="text"
                        className="form-control"
                        id="website"
                        name="website"
                        value={postData.website}
                        onChange={handleChange}
                    />
                    {/* {errors.website && (
                        <div className="alert alert-danger">
                            {errors.website}
                        </div>
                    )} */}
                </div>
                {errors?.title?.map((message, idx) => (
                    <Alert variant="warning" key={idx}>
                        {message}
                    </Alert>
                ))}
                <div className="form-group">
                    <label htmlFor="phone_number">Phone Number</label>
                    <input
                        type="text"
                        className="form-control"
                        id="phone_number"
                        name="phone_number"
                        value={postData.phone_number}
                        onChange={handleChange}
                    />
                </div>
                {errors?.title?.map((message, idx) => (
                    <Alert variant="warning" key={idx}>
                        {message}
                    </Alert>
                ))}
                <div className="form-group">
                    <label htmlFor="description">Description</label>
                    <textarea
                        className="form-control"
                        id="description"
                        name="description"
                        value={postData.description}
                        onChange={handleChange}
                    />
                </div>
                {errors?.title?.map((message, idx) => (
                    <Alert variant="warning" key={idx}>
                        {message}
                    </Alert>
                ))}
                <div className="form-group">
                    <label htmlFor="image">Image</label>
                    <input
                        type="file"
                        className="form-control"
                        id="image"
                        name="image"
                        accept="image/*"
                        onChange={handleChangeImage}
                        ref={imageInput}
                    />
                </div>
                {errors?.title?.map((message, idx) => (
                    <Alert variant="warning" key={idx}>
                        {message}
                    </Alert>
                ))}
                <br />
                <button type="submit" className="btn btn-primary">
                    Submit
                </button>
            </form>
        </div>
    );
}

export default CreatePlace;
