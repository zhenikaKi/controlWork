package src;

/** Данные по игрушке в магазине */
public class ToyInfo extends Toy {

    /** Оставшееся количество игрушек в магазине */
    private final int count;

    /**
     * Инициализация данных по игрушке.
     * @param toy Игрушка.
     * @param count Оставшееся количество игрушек в магазине
     */
    public ToyInfo(Toy toy, int count) {
        super(toy.getId(), toy.getTitle(), toy.getWeight());
        this.count = count;
    }

    @Override
    public String toString() {
        return getTitle() + ": " +
                "count=" + count +
                ", id=" + getId() +
                ", weight=" + getWeight();
    }
}
