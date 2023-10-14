import { ToSearchBranchButton } from "../../../features";
import { BankFeatures, Header } from "../../../widgets";
import "./Landing.css";

const Landing = () => {
  const rootClassName = "landing";
  return (
    <div className={rootClassName}>
      <Header />
      <main className={`${rootClassName}__main`}>
        <section className={`${rootClassName}__container`}>
          <ToSearchBranchButton />
          <BankFeatures />
        </section>
      </main>
    </div>
  );
};

export default Landing;
