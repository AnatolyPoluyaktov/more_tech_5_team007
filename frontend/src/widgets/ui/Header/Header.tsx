import { ExternalNavBar, NavBar } from "../../../features";
import "./Header.css";
import vtbLogo from "./imgs/logo_dark.png";

const Header = () => {
  const rootClassName = "header";
  return (
    <header className={rootClassName}>
      <section className={`${rootClassName}__container`}>
        <img className={`${rootClassName}__img`} src={vtbLogo} />
        <section className={`${rootClassName}__nav`}>
          <NavBar />
          <ExternalNavBar />
        </section>
      </section>
    </header>
  );
};

export default Header;
