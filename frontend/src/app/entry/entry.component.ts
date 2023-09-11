import { Component, OnInit } from '@angular/core';
import { Validators, FormBuilder } from '@angular/forms';
import { Router } from '@angular/router';
import { ResIt } from '../res-it';
import { ResItService } from '../res-it.service';

@Component({
  selector: 'app-entry',
  templateUrl: './entry.component.html',
  styleUrls: ['./entry.component.css']
})
export class EntryComponent {
	form: any;
	edit: boolean = false;
	isJob: boolean = false;
	jobs: ResIt[] = [];
	edus: ResIt[] = [];

	private date_pattern: RegExp = /^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$/;

	constructor(private fb: FormBuilder, private resItService: ResItService, private router: Router) {}

	ngOnInit(): void {
		this.form = this.fb.group({
			name: ["", Validators.required],
			id: [""],
			type: ["", Validators.required],
			title: [""],
			startdate: ["", [Validators.required, Validators.pattern(this.date_pattern)]],
			enddate: ["", Validators.pattern(this.date_pattern)],
			content: ["", Validators.required]
		});
		this.form.valueChanges.subscribe(console.log);
		this.getResIts();
	}

	onSubmit() {
		console.log(this.form);
		if (this.edit === true)
			this.onEditUpdate();
		else {
			this.resItService.addItem(this.form.value).subscribe(response => {
				console.log(response);
				this.getResIts();
			});
		}
	}

	onEdit(resIt: ResIt) {
		this.edit = true;
		console.log("edit");
		console.log(this.edit);
		console.log(resIt);
		this.form.setValue(resIt);
	}

	onEditUpdate() {
		this.edit = false;
		this.resItService.updateItem(this.form.value).subscribe(response => {
			console.log(response);
			this.getResIts();
		});
	}

	onDelete(resIt: ResIt) {
		console.log("delete");
		console.log(resIt);
		this.resItService.deleteItem(resIt.id).subscribe(response => {
			console.log(response);
			this.getResIts();
		});
	}

	selectType(event: any) {
		if (event.target.value == "job")
			this.isJob = true;
		else
			this.isJob = false;
	}

	getResIts(): void {
		this.resItService.getItems().subscribe(items => {
			console.log(items);
			this.jobs = items.filter(item => item.type == "job");
			this.edus = items.filter(item => item.type == "edu");
		});

	}
}
