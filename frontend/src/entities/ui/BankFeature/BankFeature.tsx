import { FC } from "react";
import "./BankFeature.css";
import cardImg from "./imgs/Cards.png";

interface BankFeatureProps {
  feature: string;
}

const BankFeature: FC<BankFeatureProps> = ({ feature }) => {
  const rootClassName = "bank-feature";
  return (
    <section className={rootClassName}>
      <img className={`${rootClassName}__img`} src={cardImg} />
      <p className={`${rootClassName}__feature`}>{feature}</p>
    </section>
  );
};

export default BankFeature;
