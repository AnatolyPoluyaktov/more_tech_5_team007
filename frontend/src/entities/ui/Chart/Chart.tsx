import { FC } from "react";

interface ChartProps {
  days: ChartColumn[];
}

interface ChartColumn {
  percent: number;
  time: string;
}

const Chart: FC<ChartProps> = ({ days }) => {
  return (
    <section className="chart">
      {days.map((day, index) => (
        <div className="chart__column" key={`${day.time}${index}}`}></div>
      ))}
    </section>
  );
};

export default Chart;
