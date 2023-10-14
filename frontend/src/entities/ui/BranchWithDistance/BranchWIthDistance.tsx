import { FC } from "react";
import "./BranchWithDistance.css";
import logo from "./imgs/Frame 24.png";

interface BranchWithDistanceProps {
  name: string;
  distance?: number;
  onClick?: () => void;
}

const BranchWithDistance: FC<BranchWithDistanceProps> = ({
  name,
  distance,
  onClick,
}) => {
  const clickable = onClick ? " branch-with-distance_clickable" : "";
  return (
    <section
      className={"branch-with-distance" + clickable}
      onClick={() => {
        if (onClick) onClick();
      }}
    >
      <img className="branch-with-distance__logo" src={logo} />
      <p className="branch-with-distance__address">{name}</p>
      {distance && (
        <p className="branch-with-distance__distance">{distance} м</p>
      )}
    </section>
  );
};

export default BranchWithDistance;
