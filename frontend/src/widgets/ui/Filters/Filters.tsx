import { BranchInput } from "../../../features";
import { FilterButton } from "../../../shared";
import "./Filters.css";
import {
  ClickedBankBranch,
  useBankBranchesStore,
  useFiltersStore,
} from "../..";
import { BranchWithDistance } from "../../../entities";

const Filters = () => {
  const rootClassName = "filters";
  const filtersStore = useFiltersStore();
  const bankBranchStore = useBankBranchesStore();
  const closestBranches = [
    { name: "ДО №52 «Оптиков, 34» Филиала № 7806 Банка ВТБ", distance: 630 },
  ];
  return (
    <section className={rootClassName}>
      <div className={`${rootClassName}__input`}>
        <BranchInput />
      </div>
      {bankBranchStore.clickedBranch ? (
        <ClickedBankBranch />
      ) : (
        <>
          <div className={`${rootClassName}__section`}>
            <p className={`${rootClassName}__title`}>Показать</p>
            <div className={`${rootClassName}__buttons`}>
              <FilterButton
                label="Банкоматы"
                clicked={filtersStore.atms}
                onClick={(clicked) => filtersStore.setFilter("atms", clicked)}
              />
              <FilterButton
                label="Отделения"
                clicked={filtersStore.offices}
                onClick={(clicked) =>
                  filtersStore.setFilter("offices", clicked)
                }
              />
            </div>
          </div>
          <div className={`${rootClassName}__section`}>
            <p className={`${rootClassName}__title`}>Выбрать сегмент</p>
            <div className={`${rootClassName}__buttons`}>
              <FilterButton
                label="Частным лицам"
                clicked={filtersStore.person}
                onClick={(clicked) => filtersStore.setFilter("person", clicked)}
              />
              <FilterButton
                label="Юридическим лицам"
                clicked={filtersStore.company}
                onClick={(clicked) =>
                  filtersStore.setFilter("company", clicked)
                }
              />
            </div>
          </div>
          <div className={`${rootClassName}__section`}>
            <p className={`${rootClassName}__title`}>Уточнить услуги</p>
            <div className={`${rootClassName}__buttons`}>
              <FilterButton
                label="Без выходных"
                clicked={filtersStore.withoutWeekends}
                onClick={(clicked) =>
                  filtersStore.setFilter("withoutWeekends", clicked)
                }
              />
              <FilterButton
                label="Оформление ипотеки"
                clicked={filtersStore.mortgage}
                onClick={(clicked) =>
                  filtersStore.setFilter("mortgage", clicked)
                }
              />
              <FilterButton
                label="Для людей с ограниченными возможностями"
                clicked={filtersStore.peopleWithDisabilities}
                onClick={(clicked) =>
                  filtersStore.setFilter("peopleWithDisabilities", clicked)
                }
              />
              <FilterButton
                label="Установка приложения банка"
                clicked={filtersStore.installApp}
                onClick={(clicked) =>
                  filtersStore.setFilter("installApp", clicked)
                }
              />
            </div>
          </div>
          <div className={`${rootClassName}__section`}>
            <p className={`${rootClassName}__title`}>Ближайшие офисы</p>
            <FilterButton
              label="Наименее загруженные"
              clicked={filtersStore.lessWorkload}
              onClick={(clicked) =>
                filtersStore.setFilter("lessWorkload", clicked)
              }
            />
            <div className={`${rootClassName}__closest-branches`}>
              {closestBranches.map((branch, index) => (
                <BranchWithDistance
                  key={`${branch.name}${index}`}
                  name={branch.name}
                  distance={branch.distance}
                  onClick={() => bankBranchStore.setCompleteBranch(null)}
                />
              ))}
            </div>
          </div>
        </>
      )}
    </section>
  );
};

export default Filters;
