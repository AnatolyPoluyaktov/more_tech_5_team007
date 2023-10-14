import { FC } from "react";
import "./ExternalNavLink.css";

export interface ExternalNavLinkProps {
  label: string;
  href: string;
}

const ExternalNavLink: FC<ExternalNavLinkProps> = ({ label, href }) => {
  return (
    <a className="external-nav-link" href={href}>
      {label}
    </a>
  );
};

export default ExternalNavLink;
