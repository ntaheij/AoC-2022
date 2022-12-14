use aoc_shared::input::{load_line_delimited_input_from_file, load_text_input_from_file};
use aoc_shared::parsing::parse_line_delimited;
use criterion::{black_box, criterion_group, criterion_main, BatchSize, Criterion};

use aoc_day_13::{part_one, part_two, Packet};

criterion_group!(
    benches,
    benchmark_parsing,
    benchmark_part_one,
    benchmark_part_two
);
criterion_main!(benches);

fn benchmark_parsing(c: &mut Criterion) {
    let input = load_text_input_from_file("inputs/input.txt");

    c.bench_function("parsing", |b| {
        b.iter(|| parse_line_delimited::<_, Packet>(black_box(&input)));
    });
}

fn benchmark_part_one(c: &mut Criterion) {
    let parsed = load_line_delimited_input_from_file("inputs/input.txt");

    c.bench_function("part-1", |b| {
        b.iter(|| part_one(black_box(&parsed)));
    });
}

fn benchmark_part_two(c: &mut Criterion) {
    let parsed = load_line_delimited_input_from_file("inputs/input.txt");

    c.bench_function("part-2", |b| {
        b.iter_batched(
            || parsed.clone(),
            |packets| part_two(packets),
            BatchSize::LargeInput,
        )
    });
}
