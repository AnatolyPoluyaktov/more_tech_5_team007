import { FC } from "react";
import { Link, useLocation } from "react-router-dom";
import "./NavLink.css";

export interface NavLinkProps {
  label: string;
  to: string;
}

const NavLink: FC<NavLinkProps> = ({ label, to }) => {
  const { pathname } = useLocation();
  let className = `nav-link`;
  if (pathname == to) {
    className += " nav-link__active";
  }

  return (
    <Link className={className} to={to}>
      {label}
    </Link>
  );
};

export default NavLink;
