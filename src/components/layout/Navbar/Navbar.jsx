import "./Navbar.css";
import React from 'react';
import { NavLink } from 'react-router-dom';

function Navbar(){
    return (
        <nav className="navbar">
            <div className="container-fluid">
                <div className="logo">
                    <h4>Wander<span>With</span></h4>
                </div>
                <div className="nav">
                    <NavLink to="/" className="nav-item" activeClassName="active">Home</NavLink>
                    <NavLink to="/destinations" className="nav-item" activeClassName="active">Destinations</NavLink>
                    <NavLink to="/about" className="nav-item" activeClassName="active">About</NavLink>
                    <NavLink to="/guide" className="nav-item" activeClassName="active">Guides</NavLink>
                </div>
                <div className="links">
                    <NavLink to="/login" activeClassName="active">Login</NavLink>
                    <NavLink to="/signup" activeClassName="active">Sign Up</NavLink>
                </div>
            </div>
        </nav>
    )
}

export default Navbar;
