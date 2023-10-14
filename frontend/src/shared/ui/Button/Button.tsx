import { FC } from "react";
import "./Button.css";

interface ButtonProps {
  onClick: React.MouseEventHandler<HTMLButtonElement>;
  label: string;
}

const Button: FC<ButtonProps> = ({ onClick, label }) => {
  return (
    <button className="button" type="button" onClick={onClick}>
      {label}
    </button>
  );
};

export default Button;
