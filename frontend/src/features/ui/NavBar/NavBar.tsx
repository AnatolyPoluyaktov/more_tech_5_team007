import { NavLink, NavLinkProps } from "../../../shared";
import "./NavBar.css";

const NavBar = () => {
  const rootClassName = "nav-bar";
  const navBarMeta: Array<NavLinkProps> = [
    {
      to: "/",
      label: "Частным лицам",
    },
    {
      to: "/self-employed",
      label: "Самозанятым",
    },
    {
      to: "/business",
      label: "Малый и средний бизнес",
    },
    {
      to: "/big-business",
      label: "Крупный бизнес",
    },
  ];

  return (
    <section className={rootClassName}>
      <section className={`${rootClassName}__links`}>
        {navBarMeta.map((linkMeta, index) => (
          <NavLink
            key={`${linkMeta}${index}`}
            label={linkMeta.label}
            to={linkMeta.to}
          />
        ))}
      </section>
    </section>
  );
};

export default NavBar;
