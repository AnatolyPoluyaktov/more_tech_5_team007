import { ExternalNavLink, ExternalNavLinkProps } from "../../../shared";
import "./ExternalNavBar.css";

const ExternalNavBar = () => {
  const rootClassName = "external-nav-bar";
  const externalNavBarMeta: Array<ExternalNavLinkProps> = [
    {
      href: "",
      label: "Кредиты",
    },
    {
      href: "",
      label: "Карты",
    },
    {
      href: "",
      label: "Ипотека",
    },
    {
      href: "",
      label: "Автокредиты",
    },
    {
      href: "",
      label: "Вклады и счета",
    },
    {
      href: "",
      label: "Инвестиции",
    },
    {
      href: "",
      label: "Онлайн-сервисы",
    },
    {
      href: "",
      label: "Платежи и переводы",
    },
    {
      href: "",
      label: "Другие услуги",
    },
    {
      href: "",
      label: "Привелегия",
    },
    {
      href: "",
      label: "Private Banking",
    },
  ];

  return (
    <section className={rootClassName}>
      {externalNavBarMeta.map((linkMeta, index) => (
        <ExternalNavLink
          key={`${linkMeta}${index}`}
          label={linkMeta.label}
          href={linkMeta.href}
        />
      ))}
    </section>
  );
};

export default ExternalNavBar;
