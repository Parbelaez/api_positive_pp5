import { useEffect, useState, useRef } from "react";

export const useClickOutsideToggle = () => {
    // Expand, contract the hamburger menu
    const [expanded, setExpanded] = useState(false);
    const ref = useRef(null);
    useEffect(() => {
        const handleClickOutside = (event) => {
            if (ref.current && !ref.current.contains(event.target)) {
                setExpanded(false);
            }
        };

        document.addEventListener("click", handleClickOutside);
        return () => {
            document.removeEventListener("click", handleClickOutside);
        };
    }, [ref]);

    return { expanded, setExpanded, ref };
};
