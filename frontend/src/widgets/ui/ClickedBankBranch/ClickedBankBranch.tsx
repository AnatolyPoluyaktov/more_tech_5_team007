import { useBankBranchesStore } from "../..";
import { BranchWithDistance, Services } from "../../../entities";
import { Chart } from "../../../entities/";
import { Button } from "../../../shared";
import "./ClickedBankBranch.css";
import close from "./imgs/close.png";

const ClickedBankBranch = () => {
  const rootClassName = "clicked-bank-branch";
  const bankBranchesStore = useBankBranchesStore();
  if (!bankBranchesStore.clickedBranch) {
    return;
  }
  return (
    <section className={rootClassName}>
      <section className={`${rootClassName}__container`}>
        <img
          className={`${rootClassName}__close`}
          src={close}
          onClick={() => bankBranchesStore.setCompleteBranch(null)}
        />
        <p>Офис</p>
        <BranchWithDistance name={bankBranchesStore.clickedBranch.name} />
        <p>Обслуживание частных лиц</p>
        <section className={`${rootClassName}__buttons`}>
          <Button
            label="Записаться онлайн"
            onClick={() => console.log("todo")}
          />
          <Button
            label="Проложить маршрут"
            onClick={() => console.log("todo")}
          />
        </section>
        <section className={`${rootClassName}__load-work`}>
          <p className={`${rootClassName}__load-work_title`}>
            В отделении ? окна обсуживания. График загруженности сегодня
          </p>
          <Chart days={[]} />
        </section>
        <section className={`${rootClassName}__schedule`}>
          <p className={`${rootClassName}__title`}>Время работы</p>
        </section>
        <section className={`${rootClassName}__metro`}>
          <p className={`${rootClassName}__title`}>Ближайшее метро</p>
        </section>
        <Services />
      </section>
    </section>
  );
};

export default ClickedBankBranch;
